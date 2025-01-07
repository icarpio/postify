from django.shortcuts import render, redirect
from .models import Conversation
from .forms import MessageForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import PermissionDenied

User = get_user_model()
@login_required
def send_message(request, recipient_id):
    """
    Vista para enviar un mensaje entre usuarios (incluyendo protectoras).
    """
    # Obtener al destinatario, que es el usuario asociado a la protectora
    recipient_user = get_object_or_404(User, id=recipient_id)
    

    # Crear o buscar una conversación existente entre el usuario que envía el mensaje y el destinatario
    conversation = Conversation.objects.filter(
        sender=request.user, recipient=recipient_user
    ).first()

    if not conversation:
        conversation = Conversation.objects.filter(
            sender=recipient_user, recipient=request.user
        ).first()

    if not conversation:
        conversation = Conversation.objects.create(sender=request.user, recipient=recipient_user)

    # Manejar el formulario de mensaje
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Crear el mensaje pero no guardarlo aún
            message = form.save(commit=False)
            message.sender = request.user  # Usuario que envía el mensaje
            message.conversation = conversation  # Asignar la conversación
            message.save()  # Guardar el mensaje en la base de datos
            return redirect('view_conversation', conversation_id=conversation.id)  # Redirigir a la conversación
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = MessageForm()  # Formulario vacío para GET

    # Renderizar la plantilla con los datos correctos
    return render(request, 'messagesapp/send_message.html', {
        'form': form,
        'recipient': recipient_user,  # Aquí pasamos el usuario correcto
    })


def inbox(request):
    # Obtener las conversaciones donde el usuario es remitente o destinatario
    conversations = Conversation.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    ).order_by('-created_at')
    return render(request, 'messagesapp/inbox.html', {'conversations': conversations})


User = get_user_model()

@login_required
def start_conversation(request, recipient_id):
    # Obtener la protectora (recipient)
    recipient = get_object_or_404(User, id=recipient_id)

    # Verificar si ya existe una conversación entre el usuario y la protectora
    conversation, created = Conversation.objects.get_or_create(
        sender=request.user,
        recipient=recipient
    )

    return redirect('view_conversation', conversation_id=conversation.id)



@login_required
def view_conversation(request, conversation_id):
    # Obtener la conversación donde el usuario es el sender o recipient
    conversation = get_object_or_404(
        Conversation, 
        id=conversation_id
    )

    # Verificar si el usuario actual es el sender o el recipient
    if conversation.sender != request.user and conversation.recipient != request.user:
        raise PermissionDenied  # Si no es ni el sender ni el recipient, denegar acceso

    # Obtener los mensajes de la conversación ordenados por timestamp
    messages = conversation.messages.all().order_by('timestamp')

    # Procesar el formulario de mensaje si es POST
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # El usuario actual envía el mensaje
            message.conversation = conversation  # Asociar el mensaje a la conversación
            message.save()
            return redirect('view_conversation', conversation_id=conversation.id)
    else:
        form = MessageForm()

    # Renderizar la conversación con los mensajes y el formulario
    return render(request, 'messagesapp/view_conversation.html', {
        'conversation': conversation,
        'messages': messages,
        'form': form
    })
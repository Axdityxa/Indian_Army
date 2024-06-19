# encoder/views.py
from django.shortcuts import render
from .forms import MessageForm

def encode_message(message, is_odd_day):
    odd_encoding = {chr(i): f"{i-64:02}" for i in range(65, 91)}  # A=01, B=02, ..., Z=26
    even_encoding = {chr(i): f"{i+436:03}" for i in range(65, 91)}  # A=501, B=502, ..., Z=526

    encoding = odd_encoding if is_odd_day else even_encoding

    encoded_message = []
    for char in message.upper():
        if char in encoding:
            encoded_message.append(encoding[char])
        elif char == ' ':
            encoded_message.append(' ')
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)

def encode_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            day_choice = form.cleaned_data['day_choice']
            is_odd_day = day_choice == 'odd'
            encoded_message = encode_message(message, is_odd_day)
            return render(request, 'result.html', {'encoded_message': encoded_message})
    else:
        form = MessageForm()
    return render(request, 'index.html', {'form': form})

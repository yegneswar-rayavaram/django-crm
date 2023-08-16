from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages



# - Homepage 

def home(request):

    return render(request, 'home/index.html')


# - Register a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form':form}

    return render(request, 'home/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'home/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'home/dashboard.html', context=context)


# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'home/create-record.html', context=context)


# - Update a record 

@login_required(login_url='my-login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'home/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'home/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")






def details(request):
    people=[
        {'name': 'yegneswar rayavaram', 'age':21},
        {'name':'gokul mitta', 'age':22},
        {'name':'gayatri gaddam', 'age':21},
        {'name':'bala siddharth', 'age':21}
    ]
    return render(request, "details.html", context={'peoples':people})


































































































# from django.shortcuts import render
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# # Create a dictionary of greetings and corresponding responses
# # chatbot/views.py

# # ...
# # Existing code for imports and setup

# # Create a dictionary of greetings and corresponding responses
# # chatbot/views.py

# # ...
# # Existing code for imports and setup

# # Create a dictionary of greetings and corresponding responses
# # chatbot/views.py

# # ...
# # Existing code for imports and setup

# # Create a dictionary of greetings and corresponding responses
# greetings = {
#     'hello': 'Hi there! How can I assist you',
#     'hi': 'Hello! This is AI responding',
#     'hey': 'Hey! How can I help you',
#     'how are you': 'I am doing well, thank you!',
#     'what is your name': "I'm a Chatbot, nice to meet you!",
#     'what can you do': 'I can help with answering questions and providing information!',
#     'how old are you': "I'm just a computer program, so I don't have an age!",
#     'who created you': 'I was created by Yegneswar Rayavaram',
#     'tell me a line from bhagavadgita' : 'Karmanye Vadhikaraste, Ma phaleshou kada chana',
#     'what does that line mean' : 'You have a right to perform your prescribed duty, but you are not entitled to the fruits of action. Never consider yourself to be the cause of the results of your activities, and never be attached to not doing your duty',
#     'what is the meaning of life': 'The meaning of life is a profound philosophical question!',
#     'tell me a joke': "Why don't scientists trust atoms? Because they make up everything!",
#     'what is the weather today': "I'm sorry, I am not able to provide real-time weather information.",
#     'where are you from': "I'm an AI chatbot, so I don't have a physical location!",
#     'do you like pizza': "As an AI, I don't have personal preferences, but I love helping users!",
#     'what is the capital of France': 'The capital of France is Paris.',
#     'what time is it': "I'm sorry, I don't have access to real-time information about the current time.",
#     'how do you work': "I use natural language processing algorithms to understand and respond to queries!",
#     'can you sing a song': "I'm afraid I can't sing, but I can assist you with any questions you have!",
#     'do you dream': "As an AI, I don't dream, but I'm here to help with your queries!",
#     # Add more greetings and responses as needed
# }

# def chatbot_response(request):
#     response = None

#     if request.method == 'POST':
#         user_query = request.POST.get('query', '').lower()
#         print(user_query)

#         # Check if the user query exists in the greetings dictionary
#         if user_query in greetings:
#             response = greetings[user_query]
#         else:
#             response = 'I am sorry, I do not understand. Can you rephrase your query?'
        
#         print(response)

#     return render(request, 'chatbot_response.html', {'response': response})

# # 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

# # chatbot/views.py

# import openai

# # Initialize OpenAI API with your API key
# openai.api_key = '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'

# def openai_response(request):
#     response = None

#     if request.method == 'POST':
#         user_query = request.POST.get('query', '').lower()
#         print(user_query)

#         # Make API call to OpenAI's GPT-3 model
#         try:
#             response = openai.Completion.create(
#                 engine="text-davinci-002",  # Use the appropriate GPT-3 engine
#                 prompt=user_query,
#                 max_tokens=50,  # Adjust the response length as needed
#             ).choices[0].text.strip()

#         except Exception as e:
#             print(f"Error: {e}")
#             response = 'Oops! There was an error processing your query. Please try again.'

#     print(response)

#     return render(request, 'openai_response.html', {'response': response})

# # user_query='tell me a joke'
# # response = openai.Completion.create(
# #                 engine="text-davinci-002",  # Use the appropriate GPT-3 engine
# #                 prompt=user_query,
# #                 max_tokens=50,  # Adjust the response length as needed
# #             ).choices[0].text.strip()
# # print(response)
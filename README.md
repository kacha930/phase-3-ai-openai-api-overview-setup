# OpenAI API Overview and Setup

## Learning Goals

- Assess the suitability of the various OpenAI models.
- Set up an OpenAI account.
- Set up a local environment for the API.
- Describe how token based pricing works.

## Introduction

OpenAI provides several models and their API has multiple parameters for tuning
the responses from the models. In this lesson, we will explore the GPT-3.5 model
and discuss why that’s the best one to use at the moment.

We will also be setting up a local Python environment for using the API. You
should be able to set it up for other environments such as Node.js by following
a similar pattern.

## OpenAI Models

We will be using the GPT-3.5 Turbo model in this section. It’s currently the
most cost efficient model provided by OpenAI. Its responses are just as good as
the `text-davinci-003` while using only 10% of the tokens which means each query
costs ~90% less on the GPT-3.5 model.

The GPT-4 model is more capable of following complex instructions than GPT-3.5
but it costs more. We recommend starting out with GPT-3.5 and only upgrading to
GPT-4 if you are not getting the desired responses. You can read more about
[model selection in the official docs](https://platform.openai.com/docs/guides/gpt/which-model-should-i-use)
or view
[all the available models here](https://platform.openai.com/docs/models/overview).

Both the GPT-3.5 and GPT-4 models are used for natural language processing and
generation. They use the same Chat Completion API, so it’s easy to switch models
based on requirements and tests.

## OpenAI Account Setup

We will create an OpenAI account on their developer platform and then set up an
API access key.

For the developer platform account, visit
[this link](https://platform.openai.com/signup) to sign up. You can use an email
to sign up or use one of the external account services listed there (usually
Google, Microsoft, and Apple accounts).

Your free account will have a $5 allowance for API calls with a 3 month
expiration date. If you want to use further credits, you’ll have to provide
credit card details for a usage based plan. We will discuss how pricing works
later in this lesson.

When generating the API key, make sure to save it somewhere safe before closing
the dialog since you won’t be allowed to view it afterwards.

Follow these steps to create the API key:

- Visit the [API Keys page](https://platform.openai.com/account/api-keys).
- Click on the “Create new secret key” button.
- Name it “test-key”.
- Click on the “Create secret key” button.
- Save the key somewhere secure like your password manager and never share it
  with anyone.

## Local Environment Setup

We will be using the OpenAI Python library in our environment. Here’s the
environment overview:

- Create a virtual environment.
- Install the `openai` library.
- Install the `python-dotenv` library.
- Set up a `.env` file.
- Set up a module for the AI instantiation and functions.

To get started, open up a terminal window and navigate to your developer
directory or any other directory where you want to create the virtual
environment directory.

Run the following commands to set up your environment.

```bash
# create the AI environment directory
mkdir playground-ai

# navigate into the environment directory
cd playground-ai

# set up virtual environment
pipenv --python 3.8.13

# install the OpenAI and Python-Dotenv libraries
pipenv install openai && pipenv install python-dotenv

# create a .gitignore file
touch .gitignore

# create a .env file
touch .env

# create the AI instantiation and functions file
touch ai.py

# open the folder in VSCode
code .
```

Open up the `.gitignore` file and add the following:

```
.venv/*
.pytest_cache/*
.env
```

This will ensure that the `env` file containing the secret API key isn’t
accidentally committed to the Git history and pushed to GitHub.

## Test the Environment

Let’s test out the environment by making our first request to the OpenAI API. We
will add the secret API key you generated earlier to our `.env` file and then
write code to make the request in the `ai.py` file.

Open up the `.env` file and paste in your secret API key as the value of the
`OPENAI_API_KEY`.

```bash
OPENAI_API_KEY=YOUR_SECRET_API_KEY_HERE
```

Now open up the `ai.py` file and paste in the following code:

```python
import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ["OPENAI_API_KEY"]

messages = [{"role": "user", "content": "What is the capital of New York?"}]
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )

    print(response.choices[0].message["content"])
except Exception as e:
    print(e)
```

Now enter your `pipenv` environment and run the `ai.py` file:

```bash
# start pipenv environment
pipenv shell

# run the ai.py file
python ai.py
```

This should give the following output:

```bash
The capital of New York is Albany.
```

Now you have a working environment for using the OpenAI API! We will explore how
to use this API in the next lesson.

## Token Based Pricing

Language models like GPT-4 process and produce texts in chunks called
**\*\***tokens**\*\***. A token can be as short as a single character or as long
as a word.

Both the input and output of the model uses up token allowances in your account.
Visit the [OpenAI pricing page](https://openai.com/pricing#language-models) to
check out the latest pricing information. Currently, the GPT-3.5 Turbo model
with the 4k context shows the following pricing:

- Input: $0.0015/1k tokens
- Output: $0.002/1k tokens

[This video on tokenization](https://youtu.be/sXbDXE_uD2s) will help you
understand how language models parse text.

Your free trial should give you enough token allowance to explore the API and
make a few hundred requests.

If you decide to add your credit card for a usage based account, make sure to
**also set up usage limits to avoid racking up unforeseen charges**. Visit the
[Usage Limits page](https://platform.openai.com/account/billing/limits) and add
a value to both the `Hard limit` and `Soft limit` fields. Put in a low value
like $10-$15 when starting out. You can always increase them later if needed.

## Conclusion

We have learned about various OpenAI models and set up our first Python
environment for AI development in this lesson. We will be shifting our focus to
learning how to use the API and set up AI functions for easier usage across
projects.

## Resources

- OpenAI Docs Pages:
  - [Which Model Should I Use?](https://platform.openai.com/docs/guides/gpt/which-model-should-i-use)
  - [Models Overview.](https://platform.openai.com/docs/models/overview)
  - [API Keys.](https://platform.openai.com/account/api-keys)
  - [Usage Limits.](https://platform.openai.com/account/billing/limits)
- [Words: Types, Tokens, & Tokenization video by Kevin Gimpel](https://youtu.be/sXbDXE_uD2s)

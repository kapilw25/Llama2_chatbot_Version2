# How to build a Llama 2 chatbot

Experiment with this open-source LLM from Meta

**By Chanin Nantasenamat**  
*Posted in LLMs, July 21 2023*

## Table of Contents
- [What is Llama 2?](#what-is-llama-2)
- [App overview](#app-overview)
- [Steps to Build the Chatbot](#steps-to-build-the-chatbot)
  - [Get a Replicate API token](#1-get-a-replicate-api-token)
  - [Set up the coding environment](#2-set-up-the-coding-environment)
  - [Build the app](#3-build-the-app)
  - [Set the API token](#4-set-the-api-token)
  - [Deploy the app](#5-deploy-the-app)
- [Wrapping up](#wrapping-up)

---

Generative AI has been widely adopted, and the development of new, larger, and improved LLMs is advancing rapidly, making it an exciting time for developers.

You may have heard of the recent release of Llama 2, an open source large language model (LLM) by Meta. This means that you can build on, modify, deploy, and use a local copy of the model, or host it on cloud servers (e.g., Replicate).

While it’s free to download and use, it’s worth noting that self-hosting the Llama 2 model requires a powerful computer with high-end GPUs to perform computations in a timely manner. An alternative is to host the models on a cloud platform like Replicate and use the LLM via API calls. In particular, the three Llama 2 models (llama-7b-v2-chat, llama-13b-v2-chat, and llama-70b-v2-chat) are hosted on Replicate.

In this post, we’ll build a Llama 2 chatbot in Python using Streamlit for the frontend, while the LLM backend is handled through API calls to the Llama 2 model hosted on Replicate.

🦙  
Want to jump right in? Here's the [demo app](#) and the [GitHub repo](#).

## What is Llama 2?

Meta released the second version of their open-source Llama language model on July 18, 2023. They’re democratizing access to this model by making it free to the community for both research and commercial use. They also prioritize the transparent and responsible use of AI, as evidenced by their Responsible Use Guide.

Here are the five key features of Llama 2:

- Llama 2 outperforms other open-source LLMs in benchmarks for reasoning, coding proficiency, and knowledge tests.
- The model was trained on almost twice the data of version 1, totaling 2 trillion tokens. Additionally, the training included over 1 million new human annotations and fine-tuning for chat completions.
- The model comes in three sizes, each trained with 7, 13, and 70 billion parameters.
- Llama 2 supports longer context lengths, up to 4096 tokens.
- Version 2 has a more permissive license than version 1, allowing for commercial use.

## App overview

Here is a high-level overview of the Llama2 chatbot app:

1. The user provides two inputs: (1) a Replicate API token (if requested) and (2) a prompt input (i.e. ask a question).
2. An API call is made to the Replicate server, where the prompt input is submitted and the resulting LLM-generated response is obtained and displayed in the app.

Let's take a look at the app in action:

- Go to [https://llama2.streamlit.app/](https://llama2.streamlit.app/)
- Enter your Replicate API token if prompted by the app.
- Enter your message prompt in the chat box, as shown in the screencast below.

![Llama2-chatbot-screencast](#)

## Steps to Build the Chatbot

### 1. Get a Replicate API token

Getting your Replicate API token is a simple 3-step process:

1. Go to [https://replicate.com/signin/](https://replicate.com/signin/).
2. Sign in with your GitHub account.
3. Proceed to the API tokens page and copy your API token.

### 2. Set up the coding environment

#### Local development

To set up a local coding environment, enter the following command into a command line prompt:

```bash
pip install streamlit replicate

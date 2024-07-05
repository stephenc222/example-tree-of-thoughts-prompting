# Tree of Thoughts in Python

This is the companion code repository for [my blog post](https://stephencollins.tech/posts/how-to-implement-a-tree-of-thoughts-in-python) on implementing a Tree of Thoughts in Python.

## Introduction

In this tutorial, I will walk through the implementation of a Tree of Thoughts in Python. The Tree of Thoughts is a conceptual framework that helps in exploring and evolving ideas systematically. I will use the Anthropic API to generate responses and build our tree.

## Setup

To get started, follow these steps:

1. Clone the repository:

   ```bash
   git clone git@github.com:stephenc222/example-tree-of-thoughts-prompting.git
   cd example-tree-of-thoughts-prompting
   ```

2. Set up your environment variables:

   - Create a `.env` file in the root directory of the project.
   - Add your Anthropic API key to the `.env` file:

     ```txt
     ANTHROPIC_API_KEY=YOUR_ANTHROPIC_API_KEY
     ```

3. Install the required dependencies:

   ```bash
   pip3 install python-dotenv anthropic
   ```

## Usage

To run the Tree of Thoughts implementation, execute the following command:

```bash
python3 app.py
```

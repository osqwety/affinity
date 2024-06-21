BFB Discord Bot
================

Credits
--------
- This uses the discord.py library by Rapptz.
- Contact osqwety to use my source code.

Key Features
-------------

- BFB can do all normal Discord Bot functions (ban, kick, etc)
- Has integration with llama2 AI model via ollama
- Can spam random people if you want

Installing
----------

**Python 3.8 or higher is recocmended**

To install the library, please visit their site. To utilize my code, simply download the latest release, and run the BFBBOT.py file.
**Make sure paths are set correctly.**

Integrating AI
------------------

Setup a ubuntu instance with a powerful GPU ideally:

.. code:: sh

    #Install ollama
    curl -fsSL https://ollama.com/install.sh | sh

    #Run llama3 model
    ollama run llama3

Now, in your code setup this function:

.. code:: py

    #change host URL to machines's IP on port 11434
    from ollama import Client
    def main_ai2(input2): 
        client = Client(host='http://localhost:11434')
        response = client.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': input2,
        },
        ])
        return (response['message']['content'])

Utilize the response in the bot in the form of a reply or such.



Links
------

- `Discord.py Doccumentation <https://discordpy.readthedocs.io/en/latest/index.html>`_
- `Discord.py Page <https://github.com/Rapptz/discord.py>`_
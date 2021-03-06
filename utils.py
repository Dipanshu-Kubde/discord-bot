import json
import os
import random

import discord
from discord.ext import commands

from settings import *


async def notify_user(member, message):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(message)


def mods_or_owner():
    """
    Check that the user has the correct role to execute a command
    """
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MODERATOR_ROLE_NAME))
    return commands.check(predicate)




async def get_momma_jokes():
    with open(os.path.join(DATA_DIR, "jokes.json")) as joke_file:
        jokes = json.load(joke_file)
    random_category = random.choice(list(jokes.keys()))
    insult = random.choice(list(jokes[random_category]))
    return insult

async def questions():
    with open(os.path.join(DATA_DIR, "topic.json")) as topic_file:
        topics = json.load(topic_file)
    random_category = random.choice(list(topics.keys()))
    topic = random.choice(list(topics[random_category]))
    return topic

async def truthdare():
    with open(os.path.join(DATA_DIR, "truth.json")) as truth_file:
        truths = json.load(truth_file)
    random_category = random.choice(list(truths.keys()))
    truth = random.choice(list(truths[random_category]))
    return truth

async def truthdares():
    with open(os.path.join(DATA_DIR, "dare.json")) as dare_file:
        dares = json.load(dare_file)
    random_category = random.choice(list(dares.keys()))
    dare = random.choice(list(dares[random_category]))
    return dare

async def pat():
    with open(os.path.join(DATA_DIR, "actions.json")) as actions_file:
        actions = json.load(actions_file)
    random_category = random.choice(list(actions.keys()))
    pats = random.choice(list(pats[random_category]))
    return pats


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)


def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(???`??\?????)', '(??????????\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text
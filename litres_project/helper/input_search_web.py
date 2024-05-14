from selene.core.command import *
from selene.core.wait import Command
from selene import Element
import functools


def press_sequentially(keys: str):
    def action(element: Element):
        actions = ActionChains(element.config.driver)
        actions
        functools.reduce(
            lambda actions, key: actions.send_keys_to_element(
                element.locate(),
                Keys.END + key,
            ),
            keys,
            actions,
        )
        actions.perform()

    return Command(f'press sequentially: {keys}', action)
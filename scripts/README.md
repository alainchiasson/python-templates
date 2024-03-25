# Simple single file templates

These templates are starters for simple scripts. The structure should be used to replace the quick and dirty shell scripts we do.

| File  | Descrtiption |  notes  |
|-------|--------------|---------|
| simple-template.py | Simple script that will support Typing from 3.11. | Works with python 3.7+. |
| notype-template.py | Simple, but will lnot support typing. | Works with python 2.7 as well. |
| async-template.py | Uses async run command. | Works with python 3.7+. Rune can also be replaced with other Async libs such as AnyIO and Trio  |

# Source and notes

This was taken from From : https://adamj.eu/tech/2021/10/09/a-python-script-template-with-and-without-type-hints-and-async/

A few interesting tidbits : 

- The use of SystemExit instead of just exiting points to : [Many ways to exit python](https://adamj.eu/tech/2021/10/10/the-many-ways-to-exit-in-python/)
- The __name__ == "__main__" construct - well known if you do python.

The fact that the block would not be executed if it is part of an import makes me think the argparse portion should also be in that block, but that would be for later.

In the example directory, tehre is a quick example of re-doing the cat script AND it includes a python test file. It  is a good idea to read through the article.


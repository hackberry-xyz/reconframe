# ```reconframe```
> A Python Framework for Reconnaissance.
> Distributed under the MIT license. See [LICENSE](LICENSE) for more information. 

## What is it?
```reconframe``` is a framework, not a tool. Most of its usability focuses on providing an API which can be used to create compatible and extendable tools, scripts and share information quickly.

## Why ```reconframe```?
Tools used in penetration testing are often incompatible with each other. Due to which, critical information gets lost in the midst of managing and sharing. This made a need for a framework to store and query the information. If you have been struggling with files to manage your recon data, ```reconframe``` will change your life. It stores each information in the database and provides a Python API to access the gained information.

But ```reconframe``` is not just for storing and retrieving data. It provides a proxy, filteration of data, extensive API to perform chain reactions, multi-threaded processing, utilities to generate payloads and wordlists and exporting of data in several different formats. Further, it provides a user friendly python interpreter/REPL using ptpython which gets you started in no time without learning everything about ```reconframe```.

## Installation
```sh
$ pip install reconframe
```

## Usage
The ```reconframe``` is developed with information in mind. During recon process, an information should be sharable as well as analyzable. For the same reason, ```reconframe``` comes with an embedded ptpython interpreter, a mindful API and stateful environment.

### Interpreter
The ```reconframe```'s interpreter is just a boosted Python interpreter.  ```reconframe``` injects some API utilities so that you don't have to memorize packages and modules:
```sh
$ reconframe start
```

### Python API
While the interpreter is amazing to work with, the real power of ```reconframe``` is within its API.

Following example shows how you can send a get request to example.com and store its response.

```python
from reconframe.models import http
from reconframe.project import Project

# Project helps in managing the recon data
my_project = project('example_com_recon')

# Strategies is a blueprint of a specific recon process.
@strategy
def ping():
    return http.request('https://example.com')

# This will return a Strategy object.
ping()

# This will run the strategy and return the Information object.
info = ping.run()

# The info returned from an http request contains the Response object and adding it to the project will save each information in appropriate place.
my_project.addinfo(info)

# You can also append more information to the Information object
info.foo = 'bar'

# Re adding the same information does not add duplicates to the database. So the following will only insert foo = bar in the database.
my_project.addinfo(info)

# But the information is still not updated in the database. Let's save the project to the database.
my_project.save()
```

_For more examples and usage, please refer to the [Documentation](https://reconframe.hackberry.xyz)._

## Release History
* 1.0-develop
    * Presently in development stage. See the [Kanban Board](https://github.com/hackberry-xyz/reconframe/projects/1) for more information.
* 0.1
    * Proof of Concept. Now yanked from PyPI.

## Author & Contributors

Author: Vikrant Singh Chauhan – [@0xcrypto](https://twitter.com/0xcrypto) – vi@hackberry.xyz

<a href="https://www.buymeacoffee.com/0xcrypto" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-white.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>


## Contributing
Presently reconframe is heavily under development which takes time and eventually, money. Due to lack of people, the development is completely dependent over one person - me. To solve this, I have introduced **Hackberry**. A to be registered not-for-profit organization that aims to shed my open source projects and provide financial assistance to its contributors. I am inviting people to join Hackberry and help me make more security and privacy tools.

For this project, there are several ways to contribute:

### Writing Code
1. Fork it (<https://github.com/hackberry-xyz/reconframe/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

### Spreading the Word
* [Tweet about reconframe](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fhackberry-xyz%2Freconframe&text=Meet%20reconframe%21%20A%20reconnaissance%20framework.&via=0xcrypto)
* Make a video tutorial - Good video tutorials will be listed here.
* Write a blog post - Good posts will be linked here to give your website a credible backlink.
* Write a book - Good books might be eligible for monetory rewards on Hackberry's discretion. But for now, lets have a stable release first. :) 

### Sponsoring
* Presently Hackberry is not accepting any monetory contribution. But you can still support the author and contributors directly.

TypoFixr
===============

A [Sublime Text](http://www.sublimetext.com/3) plugin that allows you to…

**determine a list of possible typos and correct them automatically**

---

- [Intro](#Intro)
- [Installation](#installation)
	- [Alternative installation methods](#alternative-installation-methods)
		- [From github](#from-github)
		- [Manually](#manually)
- [Usage](#usage)
	- [Correction](#correction)
- [Settings](#settings)
	- [Changing the highlighting color](#changing-the-highlighting-color)
	- [Keeping trailing spaces invisible](#keeping-trailing-spaces-invisible)

Intro
--------

Are you tired of seeing :

``` js
window is not defined
```

or

``` js
display is not defined
```

while coding Javascript ?

TypoFixr gets you covered. Define your own list of possible typos, and correct them on-save or manually.

Installation
------------

It is available through
[Sublime Package Contol](http://wbond.net/sublime_packages/package_control) and
this is the recommended way of installation.
Just open Packaope Control and look for TypoFirx

### Alternative installation methods

#### From github

You can install from github if you want, although Package Control automates
just that. Go to your `Packages` subdirectory under ST's data directory:

* Windows: `%APPDATA%\Sublime Text X`
* OS X: `~/Library/Application Support/Sublime Text X`
* Linux: `~/.config/sublime-text-X`
* Portable Installation: `Sublime Text X/Data`

Then clone this repository:

    git clone git://github.com/sylzys/TypoFixr.git

#### Manually

[Download](https://github.com/sylzys/TypoFixr/archive/master.zip)
the plugin as a zip. Copy the *TypoFixr* directory to its location
(see prior section).

Usage
-----

### Correction

* bind the deletion command to a keyboard shortcut:

To add a key binding, open "Preferences / Key Bindings - User" and add:

``` js
{ "keys": ["ctrl+shift+c"], "cwindow": "typofixr" }
```

With this setting, pressing <kbd>Ctrl + Shift + c</kbd> will list the typos you defined (see [settings] (#settings)) and correct them with the corresponding word of your choise throughout the current file! For OSX users, quoting wbond:
"When porting a key binding across OSes, it is common for the ctrl key on
Windows and Linux to be swapped out for super on OS X"
(eg. use "super+ctrl+c" instead).

*Beware*: the binding from this example may override one of the default ST's mapping, or one of your own defined mapping. You can look at the default bindings in
"Preferences / Key Bindings - Default", or at user's binding in "Preferences / Key Bindings - User".

Settings
-------

For the plugin to work, you first have to set your own list of typos and their replacements. Settings are stored in a configuration file, as JSON. You must use a specific
file: Go to "Preferences / Package Settings / TypoFixr / Settings
\- User" to add you custom settings. You can look at the default values in
"Settings - Default", in the same menu.

### Turning the correction on save on / off

*Default: "true"*

You may turn auto correction on file save ON / OFF. The auto correct doesn't take place while in the settings file, to prevent correction of the typos you just defined.

``` js
{ "execute_on_save": true, }
```

### Defining your own typo list

You can define your own list of typos. Just use the "replacements" settings, with the typo on the left side, and the corresponding correction on the right side.

``` js
{ "replacements": {
		"wnidow : "window",
		[...]
		"ddocument: "document"
	}
}
```
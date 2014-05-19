'''
Provides an easy way to correct code typos

See README.md for details.

@author: Sylvain Zyssman <sylzys@gmail.com>
@license: MIT (http://www.opensource.org/licenses/mit-license.php)
@since: 2014-05-15
'''

import sublime
import sublime_plugin

# Global objects
tf_settings_file = "TypoFixr.sublime-settings"
tf_settings = sublime.load_settings(tf_settings_file)
RegionsResult = []
Replacements = []

# Public: Toggles the correction on file save, depending on the settings
# No correction is done on settings' file saves
class TypoFixrListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if (tf_settings.get("execute_on_save")) and (tf_settings_file not in view.file_name()):
			view.run_command("typofixr")

# Public: Looks for "replacements" object in settings, and applies it throughout the file
class TypofixrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global tf_settings_file, tf_settings, RegionsResult, Replacements
		ListReplacements = tf_settings.get("replacements")
		for key in ListReplacements:
			RegionsResult += self.view.find_all(key, sublime.LITERAL, ListReplacements[key], Replacements)
		for i, _region in reversed(list(enumerate(RegionsResult))):
			self.view.replace(edit, _region, Replacements[i])
		sublime.status_message(str(len(RegionsResult))+" typo(s) fixed !")
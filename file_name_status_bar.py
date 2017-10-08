import sublime
import sublime_plugin
import os.path

class FileNameStatusBarCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.window().get_tabs_visible():
            self.view.set_status('fnsb', '')
        elif self.view.is_dirty():
            self.view.set_status('fnsb', os.path.basename(self.view.file_name()) + ' *')
        else:
            self.view.set_status('fnsb', os.path.basename(self.view.file_name()))

class FileNameStatusBar(sublime_plugin.EventListener):
    def on_post_save(self, view):
        view.run_command('file_name_status_bar')
    def on_modified(self, view):
        view.run_command('file_name_status_bar')
    def on_activated(self, view):
        view.run_command('file_name_status_bar')
    def on_post_window_command(self, w, command_name, args):
        if command_name == 'toggle_tabs' or command_name == 'toggle_distraction_free' or command_name == 'toggle_full_screen':
            w.active_view().run_command('file_name_status_bar')

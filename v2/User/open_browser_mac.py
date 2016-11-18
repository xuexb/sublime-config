import sublime, sublime_plugin
import webbrowser
 
url_map = {
    '/Users/xieyaowu/work/test/' : 'http://127.0.0.1/',
    'C:\\web\\html5\\' : 'http://192.168.199.2/',
}
 
class OpenBrowserMacCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        window = sublime.active_window()
        window.run_command('save')
        url = self.view.file_name()
        flag = False
        for path, domain in url_map.items():
            if url.startswith(path):
                url = url.replace(path, domain).replace('\\', '/')
                flag = True
                break

        if not flag:
            url = 'file://' + url
        webbrowser.open_new(url)
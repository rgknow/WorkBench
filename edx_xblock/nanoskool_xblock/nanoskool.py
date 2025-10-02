"""Minimal NanoSkool XBlock starter.

This XBlock renders a simple panel with a prompt and accepts a short text submission.
"""
from __future__ import annotations

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class NanoSkoolXBlock(XBlock):
    display_name = String(default="NanoSkool Olympiad Block", scope=Scope.settings, help="Title shown to learners")
    prompt = String(default="Describe your project idea in 2-3 sentences.", scope=Scope.settings)
    response = String(default="", scope=Scope.user_state)

    def student_view(self, context=None):  # noqa: D401
        html = f"""
        <div class="nanoskool-xblock">
            <h3>{self.display_name}</h3>
            <p>{self.prompt}</p>
            <textarea id="ns-response" rows="4" style="width:100%">{self.response}</textarea>
            <button id="ns-save">Save</button>
            <p id="ns-status" style="color: green;"></p>
        </div>
        """
        js = """
        function NanoSkoolXBlock(runtime, element) {
          var $ = window.jQuery;
          var handlerUrl = runtime.handlerUrl(element, 'save_response');
          $(element).find('#ns-save').on('click', function() {
            var payload = { response: $(element).find('#ns-response').val() };
            $.ajax({ type: 'POST', url: handlerUrl, data: JSON.stringify(payload), contentType: 'application/json' })
             .done(function() { $(element).find('#ns-status').text('Saved'); })
             .fail(function() { $(element).find('#ns-status').text('Error saving'); });
          });
        }
        """

        frag = Fragment(html)
        frag.add_javascript(js)
        frag.initialize_js('NanoSkoolXBlock')
        return frag

    @XBlock.json_handler
    def save_response(self, data, suffix=''):
        self.response = data.get('response', '') if isinstance(data, dict) else ''
        return {"ok": True}

from openerp import api, models, fields


class TelegramCommand(models.Model):

    _inherit = "telegram.command"

    def render_chart(self):
        pass

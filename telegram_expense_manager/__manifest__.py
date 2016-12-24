# -*- coding: utf-8 -*-
{
    "name": """Telegram Expense Manager""",
    "summary": """Expense Manager Bot""",
    "category": "Telegram",
    "images": [],
    "version": "1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    "price": 600.00,
    "currency": "EUR",

    "depends": [
        "telegram",
        "telegram_portal",
        "telegram_chart",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/telegram_command.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
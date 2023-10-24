app_name = "sms_custom_css"
app_title = "SMS Custom CSS"
app_publisher = "Shashank Shirke"
app_description = "Custom CSS functionality for Frappe & ERPNext"
app_email = "shashank@emailprovider.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/sms_custom_css/css/sms_custom_css.css"
app_include_js = "/assets/sms_custom_css/js/sms_custom_css.js"

# include js, css files in header of web template
web_include_css = "/assets/sms_custom_css/css/sms_custom_css.css"
web_include_js = "/assets/sms_custom_css/js/sms_custom_css.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sms_custom_css/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sms_custom_css/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sms_custom_css.utils.jinja_methods",
#	"filters": "sms_custom_css.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sms_custom_css.install.before_install"
# after_install = "sms_custom_css.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sms_custom_css.uninstall.before_uninstall"
# after_uninstall = "sms_custom_css.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sms_custom_css.utils.before_app_install"
# after_app_install = "sms_custom_css.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sms_custom_css.utils.before_app_uninstall"
# after_app_uninstall = "sms_custom_css.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sms_custom_css.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"sms_custom_css.tasks.all"
#	],
#	"daily": [
#		"sms_custom_css.tasks.daily"
#	],
#	"hourly": [
#		"sms_custom_css.tasks.hourly"
#	],
#	"weekly": [
#		"sms_custom_css.tasks.weekly"
#	],
#	"monthly": [
#		"sms_custom_css.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "sms_custom_css.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sms_custom_css.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sms_custom_css.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sms_custom_css.utils.before_request"]
# after_request = ["sms_custom_css.utils.after_request"]

# Job Events
# ----------
# before_job = ["sms_custom_css.utils.before_job"]
# after_job = ["sms_custom_css.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sms_custom_css.auth.validate"
# ]

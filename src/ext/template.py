import jinja2
import settings

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(settings.TEMPLATE_DIRS))

def render(template_path, template_dict):
    return env.get_template(template_path).render(template_dict)

#use django template
#def render(template_path, template_dict, debug=False):
#    from google.appengine.ext.webapp import template    
#    return template.render(find_template(template_path), template_dict, debug)

#def find_template(template_name):
#    for path in settings.TEMPLATE_DIRS:
#        fullpath = os.path.join(path, template_name);
#        if os.path.exists(fullpath):
#            return fullpath;
#    return None

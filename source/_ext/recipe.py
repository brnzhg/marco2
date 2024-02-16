
from sphinx import addnodes
from sphinx.addnodes import desc_signature, pending_xref, pending_xref_condition
from sphinx.directives import ObjectDescription, SphinxDirective
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx.util.typing import OptionSpec, TextlikeNode
from sphinx.environment import BuildEnvironment

from docutils import nodes, Node
from docutils.parsers.rst import directives


# TODO other design, tags and ing list juist nested inside recipe directive

# TODO for defining an ingredient, has tags like protein
class IngredientDirective(ObjectDescription[tuple[str, str]]):
    pass


# TODO just registers the unique recipe name
class RecipeDirective(SphinxDirective):
    pass

# TODO registers recipe tags
class RecipeTagsDirective(ObjectDescription[tuple[str, str]]):
    pass

#TODO start iwth RecipeIngList and Recipe directive, see if renders right, can associate ings with recipe, 
# next is link to ingredients
# then is directive to list out registered recipes for tags/ingredients like TodoList, ingredients for tags
# look into glossary??
class RecipeIngListDirective(ObjectDescription[tuple[str, str]]):
    option_spec: OptionSpec = {
        'no-index': directives.flag,
    }

    # TODO not putting these inside Recipe directive in case i want mulitple sections
    doc_field_types = [
        Field('recipe_ing', names=('ing', 'ingredient'), label='', has_arg=True, rolename='ing')
    ]

    #allow_nesting = False
    #has_content = True


    def handle_signature(self, sig: str, signode: desc_signature) -> tuple[str, str]:
        signode += addnodes.desc_name(text=sig)
        return sig

    #TODO maybe separate directive for recipe-tags, same for ingredient-tags, allows custom formatting of "Recipe" but mayber who cares
    #TODO need to figure out way to get register ingredients with recipe (maybe put unique recipe identifier in signature later, for now docname)
    #TODO in recipe directive, try setting self.env.ref_context, and here try reading self.env.ref_context when nesting, see what happens
    def add_target_and_index(self, name_cls: tuple[str, str], sig: str,
                             signode: desc_signature) -> None:

        recipe_domain: Domain = self.env.get_domain('recipe')
        for op in self.options:
            # does this even fucking work???
            # register each ingredient with the recipe (document)
            #recipe_domain.Register_ingredient_with_doc, domain figures out self.env.docname
            # for now maybe just match the signatures, put the recipe signature in there, or in self.options
            pass


        self.env.ref_context
        recipe_domain.


        modname = self.options.get('module', self.env.ref_context.get('py:module'))
        fullname = (modname + '.' if modname else '') + name_cls[0]
        node_id = make_id(self.env, self.state.document, '', fullname)
        signode['ids'].append(node_id)
        self.state.document.note_explicit_target(signode)

        domain = self.env.domains['py']
        domain.note_object(fullname, self.objtype, node_id, location=signode)

        canonical_name = self.options.get('canonical')
        if canonical_name:
            domain.note_object(canonical_name, self.objtype, node_id, aliased=True,
                               location=signode)

        if 'no-index-entry' not in self.options:
            indextext = self.get_index_text(modname, name_cls)
            if indextext:
                self.indexnode['entries'].append(('single', indextext, node_id, '', None))

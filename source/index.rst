.. Marco2 documentation master file, created by
   sphinx-quickstart on Tue Feb 13 15:47:02 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Marco!
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. extensions
..    ingredients - main protein, pantry,
..    recipe - difficulty

Recipes
=======


.. easier version? one recipe:recipe per document
.. recipe:recipe:: TestRecipe
   :tags: cuisine:American, health:healthy, mealtype:entree


.. recipe:inglist:: Spices
   :ing salt: .5 Tsp, optional
   :ing pepper: .5 Tsp, optional

.. recipe:ingredient:: Salt
   :tags: seasoning

.. recipe:ingredient:: Chicken
   :tags: protein

.. associate ingredients, recipe with docname, resolve through docname
.. support directives like ProteinsList, RecipesByIngredient, 
.. 


.. ambitious version
.. .. recipe:recipe:: TestRecipe
   .. recipe:inglist:: Spices
      :ing salt '.5 Tsp' opt:
      :ing pepper '.5 Tsp':
      :ing sugar '1 cup':
      :ingalt sugar honey '1 cup':
   .. recipe:inglist:: Part 1
      :ing chicken '1.5 lbs':
   **Directions Part 1**
   Just cook it dummy
   .. recipe::inglist:: Part 2
      :ing beef '1 lb':


Proteins
========



Ingredients
===========



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

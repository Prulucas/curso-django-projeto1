from django.urls import reverse, resolve
from recipes import views
# from unittest import skip
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        # reverse é a função que nos  permite adicionar uma url dinamicamente
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # @skip('Pulando testes de propósito com a decoração com skip WIP')
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        expected_return = '<h1>No recipes found here 🥲</h1>'

        response = self.client.get(reverse('recipes:home'))
        # Função decode converte bytes em uma string
        self.assertIn(expected_return, response.content.decode('utf-8'))

        # Preciso escrever mais coisas nesse teste
        # self.fail('Para que eu termine de escrever o teste')

        # WIP - Work In Progress

    def test_recipe_home_template_loads_recipe(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_context_recipes = response.context['recipes']

        content = response.content.decode('utf-8')  # testar o template
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Test recipe is_published False dont show"""
        expected_return = '<h1>No recipes found here 🥲</h1>'

        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            expected_return,
            response.content.decode('utf-8')
        )

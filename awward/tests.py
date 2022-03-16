from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class  UserTestClass(TestCase):
  def setUp(self):
    name = name.objects.create(username='andrewowalla')
    self.test = User(Bio='nice',name=name)
    
  def test_instance(self):
    self.assertTrue(isinstance(self.test,User))
    
    
class ProjectTestClass(TestCase):
    def setUp(self):
      us = us.objects.create(username='andrewowalla')
      user= User.objects.create(us=us,Bio='nice',email='andrewowalla@gmail.com')   
      self.test = Project(us =us,title='Github Search',description='Search Github repo',project_link='andrewowalla.github.io/githubsearch/',user=user)
      
    def test_instance(self):
      self.assertTrue(isinstance(self.test,Project))   
      
    def test_save(self):
      self.test.save_project()
      saved = Project.objects.all()
      self.assertTrue(len(saved)>0)
      
    def test_delete(self):
      self.test.save_project()
      self.test.delete_project()
      deleted = Project.objects.all()
      self.assertTrue(len(deleted)== 0) 
      
    def tearDown(self):
      Project.objects.all().delete()
      
      
class RateTestClass(TestCase):
  
  def setUp(self):
   us = us.objects.create(username='andrewowalla')
   user = User.objects.create(us=us,Bio='nice',email='andrewowalla@gmail.com')
   project = Project(us =us,title='Github Search',description='Search Github repo',project_link='andrewowalla.github.io/githubsearch/',user=user)  
    
   self.test = Rate (us=us,project=project,rate='nice',design=5,usability=6,content=4)
   
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Rate)) 
    
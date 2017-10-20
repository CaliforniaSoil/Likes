# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Author object: {} {} {}>".format(self.first_name, self.last_name, self.email)
    
    def __str__(self):
        return "Books in User: {}.".format(self.book.all())

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(User, related_name = "book")
    liked_by = models.ManyToManyField(User, related_name = "liked_books")
    def __repr__(self):
        return "<Book object: {} {}>".format(self.name, self.desc)
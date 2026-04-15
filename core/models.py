from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    deptName = models.CharField(max_length=100, unique=True) # department name
    deptHead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # department head userID
    def __str__(self):
        return self.deptName


class Team(models.Model):
    STATUS = [('active', 'Active'), ('disbanded', 'Disbanded')] # team status choices

    teamName = models.CharField(max_length=100, unique=True, blank=False) # team name
    teamLeader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # team leader userID
    department = models.ForeignKey(Department, on_delete=models.CASCADE) # departmentID
    teamDesc = models.TextField(blank=True) # team description
    teamStatus = models.CharField(max_length=20, choices=STATUS, default='active') # team status (active/disbanded)
    creationDate = models.DateTimeField(auto_now_add=True) # team creation date
    defunctDate = models.DateTimeField(null=True, blank=True) # team defunct date (if disbanded)

    def __str__(self):
        return self.teamName
        

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # userID
    team = models.ForeignKey(Team, on_delete=models.CASCADE) # teamID
    role = models.CharField(max_length=50) # role in the team
    joinDate = models.DateTimeField(auto_now_add=True) # date user joined the team

    class Meta:
        unique_together = ('user', 'team') # ensure a user can only be in a team once

    def __str__(self):
        return f"{self.user.username} - {self.team.teamName}"


class Repository(models.Model):
    repoName = models.CharField(max_length=100, unique=True) # repository name
    team = models.ForeignKey(Team, on_delete=models.CASCADE) # teamID
    repoURL = models.URLField() # repository URL
    platform = models.CharField(max_length=50) # repository platform
    description = models.TextField(blank=True) # repository description
    creationDate = models.DateTimeField(auto_now_add=True) # repository creation date

    def __str__(self):
        return self.repoName
    

class Dependency(models.Model):
    upstreamDep = models.ForeignKey(Team, related_name='upstream_dependencies', on_delete=models.CASCADE) # upstream teamID
    downstreamDep = models.ForeignKey(Team, related_name='downstream_dependencies', on_delete=models.CASCADE) # downstream teamID
    depType = models.CharField(max_length=50) # dependency type
    depDesc = models.TextField(blank=True) # dependency description
    depDate = models.DateTimeField(auto_now_add=True) # dependency creation date

    def __str__(self):
        return f"{self.upstreamDep} -> {self.downstreamDep}"
    

class ContactChannel(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE) # teamID
    channelType = models.CharField(max_length=50) # channel type
    channelVal = models.CharField(max_length=200) # channel value
    channelDesc = models.TextField(blank=True) # channel description
    channelDate = models.DateTimeField(auto_now_add=True) # channel creation date

    def __str__(self):
        return f"{self.team.teamName} - {self.channelType}"
    

class AuditLog(models.Model):
    ACTIONS = [('create', 'CREATE'), ('update', 'UPDATE'), ('delete', 'DELETE')] # action type choices

    action = models.CharField(max_length=20, choices=ACTIONS) # action type
    entityType = models.CharField(max_length=50) # entity type
    entityId = models.IntegerField() # entity ID
    auditDesc = models.TextField(blank=True) # description
    timestamp = models.DateTimeField(auto_now_add=True) # audit log timestamp

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.entityType} ({self.entityId})"
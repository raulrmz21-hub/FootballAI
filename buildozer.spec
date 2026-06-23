[app]
title = FootballAI
package.name = footballai
package.domain = org.ai

source.dir = .
source.include_exts = py

version = 1.0

requirements = python3==3.10.11,kivy==2.3.0

orientation = portrait

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b

p4a.fork = kivy
p4a.branch = master

#!/usr/bin/python3
'''
Top level script to start the run-time system: an actor
Created on Oct 15, 2016

Arguments
  app   : Name of parent app
  model : Name of processed (JSON) model file
  actor : Name of specific actor from the model this process will run
  args  : List of arguments for the actor of the form: --argName argValue

@author: riaps
'''
import riaps.run.main

if __name__ == '__main__':
    riaps.run.main.main()
    

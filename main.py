#!/usr/bin/env python3

import os
import requests

relative_path_to_directory = "/data/feedback/"
URL_ENDPOINT = "http://<corpweb-external-IP>/feedback/"


def get_feedback_files():
    """Returns a list of all files in the directory"""
    return [relative_path_to_directory + str(name) for name in os.listdir(relative_path_to_directory)]


def get_feedback(file):
    """Returns a dictionary of the feedback data"""
    feedback = {}
    with open(file) as f:
        feedback["title"] = f.readline().strip()
        feedback["name"] = f.readline().strip()
        feedback["date"] = f.readline().strip()
        feedback["feedback"] = f.read().strip()

    return feedback


def post_feedback(feedback):
    """Posts the feedback to the URL_ENDPOINT"""
    response = requests.post(URL_ENDPOINT, json=feedback)
    response.raise_for_status()


def main():
    """Main function"""
    for file in get_feedback_files():
        feedback = get_feedback(file)
        post_feedback(feedback)


if __name__ == '__main__':
    main()
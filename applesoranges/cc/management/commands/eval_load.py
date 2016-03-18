#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from cc.util import HeaderedRow
from cc.models import NumericExpression,NumericExpressionResponse

import os, stat, csv

class Command(BaseCommand):
    """Takes mturk repsonse CSV from [source], and loads into database."""

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, help="Path to read file from")

    def handle(self, *args, **options):
        if (options['input'] is None):
            raise CommandError("Must set input")

        with open(options['input']) as f:
            data = HeaderedRow.from_iterable(csv.reader(f))

            for datum in data:
                assignment_id = datum["AssignmentId"]
                worker_id = datum["WorkerId"]
                worker_time = datum["WorkTimeInSeconds"]
                tasks = map(int, datum["Answer.taskids"].split("\t"))
                prompts = datum["Answer.prompts"].split("\t")
                responses = datum["Answer.responses"].split("\t")

                NumericExpressionResponse.objects.bulk_create([
                    NumericExpressionResponse(
                        expression = NumericExpression.objects.get(id=task),
                        prompt = prompt,
                        description = response,
                        assignment_id = assignment_id,
                        worker_id = worker_id,
                        worker_time = worker_time,
                        approval = False,
                        )
                    for (task, prompt, response) in zip(tasks, prompts, responses)])


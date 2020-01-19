#!/bin/sh
#
# QUEUEの名前を引数で受け取りそのURLを返す
#

SQS_QUEUE_NAME=$1


SQS_QUEUE_URL=$( \
  aws sqs get-queue-url \
    --queue-name ${SQS_QUEUE_NAME} \
    --output text\
  )

echo ${SQS_QUEUE_URL}
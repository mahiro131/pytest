#!/bin/sh
#
# QUEUEのURLを引数として受け取り、
# メッセージの数を返す

SQS_QUEUE_URL=$1

SQS_NUM_MESSAGE=$( \
    aws sqs get-queue-attributes \
    --queue-url ${SQS_QUEUE_URL} \
    --attribute-names ApproximateNumberOfMessages \
    # --output text | # shellで数字だけ返すか、python側でjsonとして処理するか
    # cut -f 2
    )

echo ${SQS_NUM_MESSAGE}
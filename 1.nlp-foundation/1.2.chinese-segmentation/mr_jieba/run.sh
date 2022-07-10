
HADOOP_CMD="/home/parallels/Tools/hadoop-2.6.5/bin/hadoop"
STREAM_JAR_PATH="/home/parallels/Tools/hadoop-2.6.5/share/hadoop/tools/lib/hadoop-streaming-2.6.5.jar"

INPUT_FILE_PATH_1="/music.data"
OUTPUT_Z_PATH="/output_wordseg"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_Z_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_Z_PATH \
    -mapper "python map_seg.py" \
    -jobconf "mapred.reduce.tasks=0" \
    -jobconf "mapreduce.map.memory.mb=4096" \
    -jobconf  "mapred.job.name=jieba_fenci_demo" \
    -file "./jieba.tgz" \
    -file "./map_seg.py"



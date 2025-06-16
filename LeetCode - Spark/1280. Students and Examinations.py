import pandas as pd
from pyspark.sql.functions import count, when

# 1280. Students and Examinations

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
    {'student_id': 'Int64', 'student_name': 'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'],
        [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
    {'student_id': 'Int64', 'subject_name': 'object'})

students_df = spark.createDataFrame(students)
subjects_df = spark.createDataFrame(subjects)
examinations_df = spark.createDataFrame(examinations)

result_df = students_df\
    .alias("std")\
        .join(subjects_df.alias("sub"), how="cross")\
            .join(examinations_df.alias("exam"), ((col("std.student_id")==col("exam.student_id")) & (col("sub.subject_name")==col("exam.subject_name"))),"left")\
                .withColumn("attended_exams",when(col("exam.subject_name").isNull(),0).otherwise(1))\
                    .groupBy(col("std.student_id"),col("std.student_name"),col("sub.subject_name"))\
                        .agg(count(when(col("exam.subject_name").isNotNull(),col("sub.subject_name"))).alias("attended_exams"))\
                            .orderBy(col("std.student_id").asc(),col("sub.subject_name").asc())

result_df.display()


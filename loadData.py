import psycopg2 as postgresdb

def getConnection():
    return postgresdb.connect(
        host='localhost',
        database='grafana',
        user='postgres',
        password='postgres'
        )

def main():
    connection = getConnection()
    cur = connection.cursor()
    cur.execute('DELETE FROM feedback;')
    cur.execute('ALTER SEQUENCE feeback_id_seq RESTART WITH 1;')
    count = 0
    with open('Feebback_Responses.csv','r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            print(count,'=>',values)
            INSERT_QUERY = "INSERT INTO feedback(datetimestamp, teacher_name, activity_covered, total_students, total_female_students, total_groups_formed, groups_completed_activity, students_review_after_activity, additional_comments) VALUES (<1>, <2>, <3>, <4>, <5>, <6>, <7>, <8>, <9>)"
            INSERT_QUERY = INSERT_QUERY.replace('<1>', '\''+values[0]+'\'').replace('<2>', '\''+values[1]+'\'').replace('<3>', '\''+values[2]+'\'').replace('<4>', values[3]).replace('<5>', values[4]).replace('<6>', values[5]).replace('<7>', values[6]).replace('<8>', '\''+values[7]+'\'').replace('<9>', '\''+values[8]+'\'')
            cur.execute(INSERT_QUERY)
            print('Inserted Row',count)
            count += 1
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
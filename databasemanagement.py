from random import randrange
import sqlite3


class Time():
    def __init__(self, scramble, time):

        self.scramble = scramble
        self.time = time
        self.avgo5 = 5
        self.avgo12 = 12
        self.db = Database()
        self.calc_avgo12()
        self.calc_avgo5()

    def calc_avgo5(self):
        table = self.db.get_table()
        times = []
        times.append(self.time)
        for i in reversed(table):
            times.append(i[2])
            if len(times) == 5:
                break
        self.avgo5 = sum(times)/len(times)

    def calc_avgo12(self):
        table = self.db.get_table()
        times = []
        times.append(self.time)
        for i in reversed(table):
            times.append(i[2])
            if len(times) == 12:
                break
        self.avgo12 = sum(times)/len(times)

    def __repr__(self):
        return str(self.time)


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        # self.create_table()

    def create_table(self):
        # create a table that holds time information
        # solve count  -  scramble  -  time  -  avgo5  -  avgo12
        # INTEGER            TEXT        REAL    REAL        REAL
        self.c.execute("""CREATE TABLE times(
                    solve_count integer,
                    scramble text,
                    time real,
                    avgo5 real,
                    avgo12 real
                    )""")

        # print('times' in tables[0])

    def get_table(self):
        self.c.execute("SELECT * FROM times")
        all_times = self.c.fetchall()
        return all_times

    def insert_time(self, time: Time):
        with self.conn:
            self.c.execute("SELECT * FROM times")
            all_times = self.c.fetchall()
            solve_count = len(all_times)+1
            self.c.execute("INSERT INTO times VALUES (:solve_count, :scramble, :time, :avgo5, :avgo12)",
                           {'solve_count': solve_count, 'scramble': str(time.scramble), 'time': time.time, 'avgo5': time.avgo5, 'avgo12': time.avgo12})

    def print_table(self):
        import pprint
        pprint.pprint(self.get_table())

    def get_time_by_solve_count(self, solve_count):
        self.c.execute("SELECT * FROM times WHERE solve_count = :solve_count",
                       {'solve_count': solve_count})
        return self.c.fetchone()

    def remove_time(self, solve_count):
        with self.conn:
            self.c.execute("""DELETE from times WHERE solve_count=:solve_count         
                    """, {'solve_count': solve_count})
        self.fix_solve_counts()
        self.fix_avgs(solve_count)

    def fix_solve_counts(self):
        table = self.get_table()
        for i in range(len(table)):
            solve_count = i+1
            if not solve_count == table[i][0]:
                with self.conn:
                    self.c.execute("""UPDATE times SET solve_count=:new_solve_count WHERE solve_count=:solve_count""", {
                        'new_solve_count': solve_count, 'solve_count': table[i][0]})

    def fix_avgs(self, start_point):
        # * fix avg of 5 s
        table = self.get_table()

        for point in range(start_point, start_point+4):
            times = []
            for i in reversed(table[:point]):
                times.append(i[2])
                if len(times) == 5:
                    break
            new_avgo5 = sum(times)/len(times)
            self.c.execute("""UPDATE times SET avgo5= :avgo5 WHERE solve_count=:solve_count
                        """, {'avgo5': new_avgo5, 'solve_count': point})
        # * fix avg of 12 s
        for point in range(start_point, start_point+11):
            times = []
            for i in reversed(table[:point]):
                times.append(i[2])
                if len(times) == 12:
                    break
            new_avgo12 = sum(times)/len(times)
            self.c.execute("""UPDATE times SET avgo12= :avgo12 WHERE solve_count=:solve_count
                        """, {'avgo12': new_avgo12, 'solve_count': point})

    def last_time(self):
        table = self.get_table()
        return table[len(table)-1]

# d = Database()
# d.print_table()
# d.fix_avgs(8)
# for _ in range(20):
#     t = Time('ABC', randrange(15, 20))
#     d.insert_time(t)

# for i in range(20, 0, -1):
#     d.remove_time(i)
# t = Time('ABC', 17.5)
# print(d.get_time_by_solve_count(6))
# t.calc_avgo12()
# d.insert_time(t)
# print(d.get_time_by_solve_count(30))
# d = Database()
# d.remove_time(3)
# d.print_table()


# conn = sqlite3.connect('database.db')

# c = conn.cursor()


# c.execute("INSERT INTO times VALUES (?, ?, ?, ?, ?)",
#           (t.solve_count, t.scramble, t.time, t.avgo5, t.avgo12))
# conn.commit()

# c.execute("INSERT INTO times VALUES (:solve_count, :scramble, :time, :avgo5, :avgo12)",
#           {'solve_count': t2.solve_count, 'scramble': t2.scramble, 'time': t2.time, 'avgo5': t2.avgo5, 'avgo12': t2.avgo12})
# conn.commit()
# insert_time(15.66, 'K L M')
# insert_time(24.8, 'B C D')
# insert_time(55.2, 'V Y Z')
# if __name__ == '__main__':
#     c.execute("SELECT * FROM times")
#     print(c.fetchall())
# remove_time(2, c.fetchall())
# c.execute("SELECT * FROM times")
# print(c.fetchall())
# print(get_last_5(2))

#! before change you need to commit to the connection
# conn.commit()

# conn.close()

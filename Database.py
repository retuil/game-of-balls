import pygame
import sqlite3
from SortedGroup import SortedGroup


class Database:
    def __init__(self, saved):
        self.connection = sqlite3.connect("database")
        self.cur = self.connection.cursor()
        self.redact(saved)

    def redact(self, saved):
        result1 = self.cur.execute("""SELECT score FROM record""").fetchall()
        result = []
        for i in result1:
            i = int(*i)
            result.append(i)

        for elem in result:
            if saved >= int(elem):
                m = result[result.index(elem):][:-1]
                result = result[:result.index(elem)] + [int(saved)] + m
                break
        for elem in result:
            self.cur.execute("""UPDATE record
                SET score = ?
                WHERE ID = ?""", (elem, result.index(elem) + 1)).fetchall()

        self.connection.commit()
        self.connection.close()

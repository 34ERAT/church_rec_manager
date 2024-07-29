class TABLE_QUERIES():

    BAPTISM_ = """
    CREATE TABLE `BAPTISM` (
        `BAPTISM_NO` int NOT NULL,
        `godchild` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
        `MOTHER_NAMES` varchar(255) DEFAULT NULL,
        `FATHER_NAMES` varchar(255) DEFAULT NULL,
        `file_url` varchar(255) DEFAULT NULL,
        `upload_time` datetime DEFAULT NULL,
        PRIMARY KEY (`BAPTISM_NO`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CONFIRMATION_ = """
    CREATE TABLE `CONFIRMATION` (
        `CONFIMARTION_ID` varchar(255) NOT NULL,
        `CONFIMATION_NO` int DEFAULT NULL,
        `DATE_` date DEFAULT NULL,
        `MOTHER` varchar(50) DEFAULT NULL,
        `FATHER` varchar(50) DEFAULT NULL,
        `NO_MEN_BAPT` int DEFAULT NULL,
        `G_mother` varchar(50) DEFAULT NULL,
        `G_FATHER` varchar(50) DEFAULT NULL,
        `PRIEST` varchar(50) DEFAULT NULL,
        `BAPTUM_DIE` varchar(50) DEFAULT NULL,
        PRIMARY KEY (`CONFIMARTION_ID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    DEATH_ = """
    CREATE TABLE `DEATH` (
        `Death_id` varchar(255) NOT NULL,
        `Names` varchar(255) DEFAULT NULL,
        `upload_date` datetime DEFAULT NULL,
        `file_url` varchar(255) DEFAULT NULL,
        PRIMARY KEY (`Death_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    MARRIAGE_ = """
    CREATE TABLE `MARRIAGE_` (
        `marriage_id` varchar(255) NOT NULL,
        `h_name` varchar(255) DEFAULT NULL,
        `W_name` varchar(255) DEFAULT NULL,
        `upload_date` datetime DEFAULT NULL,
        `file_url` varchar(255) DEFAULT NULL,
        PRIMARY KEY (`marriage_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    def get_table_queries(self):
        return [self.MARRIAGE_,self.DEATH_,self.CONFIRMATION_,self.BAPTISM_]

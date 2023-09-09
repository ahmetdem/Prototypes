#include <iostream>
#include <sqlite3.h>
#include <vector>
#include <string>

std::vector<std::string> split(std::string& str, char delim)
{
    std::vector<std::string> tokens;
    size_t prev = 0, pos = 0;

    do
    {
        pos = str.find(delim, prev);

        if (pos == std::string::npos)
            pos = str.length();

        std::string token = str.substr(prev, pos - prev);

        if (!token.empty())
            tokens.push_back(token);

        prev = pos + 1;

    } while (pos < str.length() && prev < str.length());

    return tokens;
}


void insert_to_db(std::string data)
{
    sqlite3* DB;
    int exit = sqlite3_open("visitor.db", &DB);
    char* messaggeError;

    if (exit != SQLITE_OK) {
        std::cout << messaggeError << std::endl;
        sqlite3_free(messaggeError);
    }
    
    std::vector<std::string> tokens = split(data, ';');
    std::string sql = "INSERT INTO PERSON VALUES(" + tokens[0] + ", '" + tokens[1] + "', '" + tokens[2] + "', " + tokens[3] + ", '" + tokens[4] + "');";


    /*print the tokens*/
    for (auto& s : tokens)
        std::cout << s << " ";

    std::cout << "\n" << std::endl;


    exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messaggeError);

    if (exit != SQLITE_OK) {
        std::cerr << "Error INSERT" << std::endl;
        std::cout << messaggeError << std::endl;
        sqlite3_free(messaggeError);
    }
    else
        std::cout << "Records created Successfully!" << std::endl;
}

// int main(int argc, char** argv)
// {
// 	sqlite3* DB;
// 	// std::string sql = "CREATE TABLE PERSON("
// 	// 				"ID INT PRIMARY KEY	 NOT NULL, "
// 	// 				"NAME		 TEXT NOT NULL, "
// 	// 				"SURNAME		 TEXT	 NOT NULL, "
// 	// 				"AGE		 INT	 NOT NULL, "
// 	// 				"Email	 CHAR(50)); ";


//     int exit = sqlite3_open("example.db", &DB);
//     char* messaggeError;

//     // exit = sqlite3_exec(DB, sql.c_str(), NULL, 0, &messaggeError);


// 	if (exit != SQLITE_OK) {
// 		std::cout << messaggeError << std::endl;
// 	}
// 	// else
// 	// 	std::cout << "Table created Successfully" << std::endl;

// 	sqlite3_close(DB);
// 	return (0);
// }

class Solution
{
public:
    string validIPAddress(string queryIP)
    {
        std::vector<string> vec;

        string queryIP_copy = queryIP;
        if (queryIP_copy.find(".") != std::string::npos)
        {
            while (queryIP_copy.find(".") != std::string::npos)
            {
                int pos = queryIP_copy.find(".");
                vec.push_back(queryIP_copy.substr(0, pos));
                queryIP_copy.erase(0, pos + 1);
            }
            vec.push_back(queryIP_copy.substr(0, 50));
        }
        else if (queryIP_copy.find(":") != std::string::npos)
        {
            while (queryIP_copy.find(":") != std::string::npos)
            {
                int pos = queryIP_copy.find(":");
                vec.push_back(queryIP_copy.substr(0, pos));
                queryIP_copy.erase(0, pos + 1);
            }
            vec.push_back(queryIP_copy.substr(0, 50));
        }
        else
        {
            return "Neither";
        }

        if (vec.size() == 4)
        {
            // IPv4 check
            for (int i = 0; i < 4; i++)
            {
                string bucket = vec.at(i);
                // Check that the size of each bucket is allowed
                if (bucket.size() > 3 || bucket.size() == '0')
                {
                    return "Neither";
                }
                if (bucket.size() > 1 && bucket.at(0) == '0')
                {
                    return "Neither";
                }
                // Check that all values in the string are numbers
                std::list<char> nums = {'0', '1', '2', '3', '4',
                                        '5', '6', '7', '8', '9'};
                for (int j = 0; j < bucket.size(); j++)
                {
                    if (std::find(nums.begin(), nums.end(), bucket.at(j)) ==
                        nums.end())
                    {
                        return "Neither";
                    }
                }
                try
                {
                    if (std::stoi(bucket) > 255)
                    {
                        return "Neither";
                    }
                }
                catch (const std::invalid_argument &e)
                {
                    return "Neither";
                }
            }
            return "IPv4";
        }
        else if (vec.size() == 8)
        {
            // IPv6 check
            for (int i = 0; i < 8; i++)
            {
                string bucket = vec.at(i);
                // Check for correct length
                if (bucket.size() == 0 || bucket.size() > 4)
                {
                    return "Neither";
                }
                std::list<char> nums = {'0', '1', '2', '3', '4', '5', '6', '7',
                                        '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
                                        'A', 'B', 'C', 'D', 'E', 'F'};
                for (int j = 0; j < bucket.size(); j++)
                {
                    if (std::find(nums.begin(), nums.end(), bucket.at(j)) ==
                        nums.end())
                    {
                        return "Neither";
                    }
                }
            }
            return "IPv6";
        }
        return "Neither";
    }
};
#include <iostream>
#include <string>
#include <map>

auto main() -> int {
    std::map<std::string, std::string> m;
    m["flag"] = std::string("flag{this_is_flag!}");
    m["real_flag"] = std::string("flag{this_is_real_flag!}");
    std::cout << m["flag"] << " " << m["real_flag"] << std::endl;
    return 0;
}

#include <cassert>
#include <iostream>
#include <string>

#include "cctz/time_zone.h"
#include "cctz/civil_time.h"

bool should_use_iceberg_timestamptz_utc_fast_path(const cctz::time_zone& timezone) {
    return timezone == cctz::utc_time_zone();
}

void test_timezone(const std::string& tz_name) {
    cctz::time_zone tz;
    bool ok = cctz::load_time_zone(tz_name, &tz);

    assert(ok);

    std::cout << "timezone = " << tz_name
              << ", fast_path = "
              << should_use_iceberg_timestamptz_utc_fast_path(tz)
              << std::endl;
}

int main() {
    // exact UTC
    test_timezone("UTC");

    // aliases
    test_timezone("Etc/UTC");
    test_timezone("Etc/GMT");
    test_timezone("GMT");

    // non-UTC
    test_timezone("Asia/Shanghai");
    test_timezone("America/New_York");

    return 0;
}
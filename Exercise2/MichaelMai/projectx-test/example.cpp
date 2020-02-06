#include "gmock/gmock.h"

#include "example.h"

using namespace testing;

namespace projectx::tests
{
	TEST(ExampleTests, Example) {
		projectx::Example example{};
        ASSERT_THAT(example.getValue(), Eq(99));
	}


	
}

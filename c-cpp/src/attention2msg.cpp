#include <iostream>
#include <vector>

class AttentionAdder
{
public:
	AttentionAdder();
	~AttentionAdder(){};
	void run();
protected:
	std::vector<std::string> top, base, bottom;
	std::vector<std::vector<std::string>> attention;
	std::string input_msg;
	
	std::string wrap_msg();
	void test();
};

AttentionAdder::AttentionAdder()
{
	std::cout << "input message: ";
	std::cin >> input_msg;
	top = {"＿", "人", "＿"};
	base = {"＞", "＜"};
	bottom = {"ー", "Ｙ", "ー"};
	attention = {top, base, bottom};
}

std::string AttentionAdder::wrap_msg()
{
	std::vector<std::string> msg;
	int msg_len;
	msg_len = input_msg.size();
	for (char& c: input_msg)
	{
		std::cout << c << std::endl;
	}

	return "a";
}

void AttentionAdder::test()
{
	wrap_msg();
}

void AttentionAdder::run()
{
	if (input_msg == "test")
	{
		test();
	}
}

int main()
{
	AttentionAdder attention;
	attention.run();

	return 0;
}

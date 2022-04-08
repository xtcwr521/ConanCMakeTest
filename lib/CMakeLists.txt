add_library(MyLib src/CustomizedWidget.cpp src/Adder.cpp include/CustomizedWidget.h)
target_include_directories(MyLib PUBLIC include/)
target_link_libraries(MyLib PUBLIC Qt6::Widgets)

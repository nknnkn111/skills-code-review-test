import unused from "./util";
const a = "测试变量";

// 超长函数，多层嵌套
function doSomething(flag1, flag2, flag3) {
    if (flag1) {
        if (flag2) {
            if (flag3) {
                console.log(a + unused);
            }
        }
    }
    // 无try-catch捕获异常
    const data = JSON.parse("{{{{");
    return data;
}
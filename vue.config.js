const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true
})
// module.exports = {
//   lintOnSave:false,  //关闭语法检查
// }

// 跨域配置
module.exports = {
    lintOnSave:false,
    devServer: {                //记住，别写错了devServer//设置本地默认端口  选填
        port: 2333,
        proxy: {                 //设置代理，必须填
            '/api': {              //设置拦截器  拦截器格式   斜杠+拦截器名字，名字可以自己定

                // 后端的地址，通过 /api/xxx访问后端，弹幕有去掉api成功的
                target: 'http://127.0.0.1:1234',     //代理的目标地址
                changeOrigin: true,              //是否x`设置同源，输入是的
                pathRewrite: {                   //路径重写
                    '^/api': ''                     //选择忽略拦截器里面的内容
                }
            }
        }
    }
}

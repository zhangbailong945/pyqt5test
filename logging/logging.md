## python日志库logging

## 日志级别
    python标准库用作记录日志，默认分为六种日志级别。NOTSET(0),DEBUG(10),INFO(20),WARNING(30),ERROR(40),CRITICAL(50)。

## logging流程
    Logger,日志，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。
    LogRecord,日志处理器，将日志传到相应的处理器。
    Filter,过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
    Handler,处理器，将（日志记录器产生的）日志记录发送至合适的目的地。
    Formatter，格式化器，指明了最终输出中日志记录的布局。

## 基本使用
logging使用非常简单，使用basicConfig()方法就能满足基本的使用需求，如果方法没有传入参数，会根据默认的配置创建Logger对象，默认的日志级别设置为WARNING。
参数：
*filename 日志输出到文件的文件名
*文件模式 r[+]、w[+]、a[+]
*format 日志输出格式
*datefat 日志附带日期时间格式
*style 格式占位符默认%和{}
*level 设置日志输出级别
*stream 定义输出流，用来初始化StreamHandler对象，不能filename一起使用，否则会ValueError异常
*handles 定义处理器，用来创建Handler对象，不能喝filename,stream参数一起使用，否则抛出ValueError异常



设计原则

* KISS (Keep It Simple, Stupid) — 类和方法的职责应足够简单，能用 10 行搞定的不要写 50 行
* DRY (Don't Repeat Yourself) — 相同的配置注册逻辑或条件判断不应在多个 -spring-boot 模块间重复拷贝
* SRP (单一职责原则) — 一个类不应同时承担配置解析、Bean 注册和事件监听等无直接关联的职责
* OCP (开闭原则) — 扩展点应对扩展开放、对修改封闭，而非靠 if/else 判断类型
* LSP (里氏替换原则) — abstract class 的子类不应重写父类方法并违反父类约定的前置/后置条件
* ISP (接口隔离原则) — 接口不应包含调用者不需要的方法，比如一张万用 SPI 通吃所有场景
* DIP (依赖倒置原则) — 自动配置应依赖接口而非具体实现，消费者不应直接 new 具体类
* YAGNI (你不会需要它) — 不存在引用者的 @SpiImpl 实现和未被使用的自动配置是典型过度设计
* LoD (得墨忒耳法则) — 方法只应跟直接朋友说话，不应穿透多层 getter 去拿隔着两层的数据
* CRP (组合优于继承) — 行为复用应优先用委托/组合（如 Spring *Template）而非 extends
* FFP (快速失败原则) — 启动期检测到配置冲突就抛明确异常，而非运行时静默失败
* PoLA (最少惊讶原则) — 自动配置命名、文件路径、条件行为应符合使用者的直觉预期
* SLAP (单一抽象层次原则) — 方法内不应把 IO/反射等基础设施调用和业务逻辑混在同一层级
* TDA (Tell, Don't Ask) — 对象应自己判断状态（ctx.hasTenant()）而非让调用者取出数据来问
* POJO (清洁架构) — 领域对象不应依赖框架注解或基础设施类
* Defensive Programming (防御性编程) — 公共方法入口先断言参数合法性，别用到才抛 NPE
* Prefer Immutability (优先不可变) — final 字段优先于 mutable，减少并发隐患和意外修改
* Prefer Concurrent Utilities (优先并发工具) — synchronized 优先用 ReentrantLock / AtomicReference 替代
* Test Behavior (测试行为而非实现) — 测试断言输出结果，不验证内部方法调用顺序或 mock 细节
* Exception Hierarchy (异常层次化) — 自定义异常基于统一基类按场景细分，不混用
* Optional Not as Parameter (Optional 不作参数) — Optional<T> 只作返回类型，不作方法参数
* Static Factory (静态工厂优于构造器) — 构造复杂的类暴露 of/from/valueOf 工厂方法
* Log Level Discipline (日志分级纪律) — 生命周期事件用 INFO/WARN，追踪用 DEBUG/TRACE
* Exceptions Not for Control Flow (异常不用于流程控制) — try/catch 不应代替 if 做分支判断
* Try-with-Resources — IO/连接资源用 try-with-resources 自动关闭，不依赖 finally
* Cache Invalidation (缓存有失效策略) — 内存缓存应有明确 TTL 或淘汰机制
* Logger Naming (Logger 命名统一) — 全仓库统一用 logger 或 log（当前两种写法并存）
* Least Exposure (最少暴露原则) — 可见性从窄到宽，只开放必须被外部调用的 API
* No Static Mutable Collections (避免静态可变集合) — static final 集合跨测试共享状态破坏隔离性
* Test Naming Convention (测试命名一致) — UT 后缀统一用 *Tests.java（当前 29 个 *Test.java 未遵循）
* Return Empty Collections (集合返回不 null) — 集合/数组方法返回空集合而非 null
* Parameter Object (参数对象模式) — 3+ 个反复组合的参数应封装为值对象
* Design by Contract (契约式设计) — 接口应声明前置条件和后置条件，子类不应违反

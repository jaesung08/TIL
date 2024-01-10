package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello";
    }
    @GetMapping("hello-mvc") // http://localhost:8080/hello-mvc?name=(이름)
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }

    @GetMapping("hello-string") // http://localhost:8080/hello-string?name=js
    @ResponseBody
    public String helloString(@RequestParam("name") String name ) {
        return "hello " + name;
    }

    @GetMapping("hello-api") // http://localhost:8080/hello-api?name=js
    @ResponseBody               // html이 없고 객체가 있기때문에 json형식으로 반환
    public Hello helloApi(@RequestParam("name") String name ) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }
    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
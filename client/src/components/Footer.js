import { FaHeart } from "react-icons/fa6";
import { BsLinkedin } from "react-icons/bs";
import { BsGithub } from "react-icons/bs";


const Footer = () => {
  return (
    <div id="footer">
        <span>Made with <FaHeart /> by Kat Tannehill</span>
        <span>
            <a href="https://flatironschool.com/"><strong>//</strong></a>
            <a href="https://www.linkedin.com/in/kat-tannehill/">
            <BsLinkedin />
            </a>
            <a href="https://github.com/ktannehill">
                <BsGithub />
            </a>
        </span>
    </div>
  )
}

export default Footer
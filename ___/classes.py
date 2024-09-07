from ctransformers import AutoModelForCausalLM


class Model(object):
    model = None
    llm = None
    options = {
        'orca': {
            'name': 'zoltanctoth/orca_mini_3B-GGUF',
            'file': 'orca-mini-3b.q4_0.gguf'
        },
        'llama2': {
            'name': 'TheBloke/Llama-2-7b-Chat-GGUF',
            'file': 'llama-2-7b-chat.Q5_K_M.gguf'
        },
        'llama3': {
            'name': 'SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF',
            'file': 'meta-llama-3.1-8b-instruct.Q2_K.gguf'
            # 'name': "Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2-GGUF",
            # 'file': "Llama-3.1-8B-Lexi-Uncensored_V2_F16.gguf"
            # 'name': 'lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF',
            # 'file': 'Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf'
        }
    }

    def set_llm(self, option):
        if option == self.model:
            return
        self.model = option
        self.llm = AutoModelForCausalLM.from_pretrained(
            self.options[option]['name'], model_file=self.options[option]['file']
        )
        print(f'\033[94mWARNING: {option} model set!!!\033[m')

    def get_llm(self):
        return self.llm

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Model, cls).__new__(cls)
            cls.set_llm(cls, 'orca')
        return cls.instance

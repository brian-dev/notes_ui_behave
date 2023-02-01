class Product:
    def __init__(self, context, product_name):
        self.context = context
        self.product = self.context.yaml_utils.get_product_info(product_name)
        self.title = self.product['title']
        self.description = self.product['description']
        self.price = self.product['price']
        self.cart_btn_id = self.product['add_to_cart_btn_id']
        self.img_txt = self.product['img_alt_txt']

    def get_product_title(self):
        return self.title

    def get_product_desc(self):
        return self.description

    def get_product_price(self):
        return self.price

    def get_cart_btn_id(self):
        return self.cart_btn_id

    def get_img_txt(self):
        return self.img_txt
